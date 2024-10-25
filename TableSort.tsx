
class TableSort{
    // common var
    static version: string = '1.0.0';
    static instance: TableSort[] = [];


    table: HTMLElement;
    thead: boolean;
    options: any;
    current?: HTMLElement;
    col?: number;

    constructor(el: HTMLElement | string, options:any={}){
        el = Util.getElem(el) as HTMLElement;
        if (!(this instanceof TableSort)) return new TableSort(el,options);
        if (!el||!(el instanceof HTMLTableElement)) throw new Error('Element must be a table');
        
        this.init(el,options,TableSort.instance.length);
        TableSort.instance.push(this);
    }

    init(el:HTMLElement,options:any,id:number){
        let that = this;
        let firstRow: HTMLTableRowElement | null = null;
        let defaultSort: HTMLElement | null = null;
        let i : number;
        let cell: HTMLElement | undefined;
        let getHead: HTMLElement|null;
        that.table = el;
        that.thead = false;
        that.options = options;
        if (el instanceof HTMLTableElement && el.rows.length >0) {
            if (el.tHead && el.tHead.rows.length>0){
                for (i = 0 ; i < el.tHead.rows.length;i++){
                    if (el.tHead.rows[i].getAttribute('data-sort-method')=== 'thead'){
                        firstRow = el.tHead.rows[i];
                        break;
                    }
                }
                if(!firstRow){
                    firstRow = el.tHead.rows[el.tHead.rows.length - 1];
                }
                that.thead = true;
            } else{
                firstRow = el.rows[0];
            }
        }
        getHead = el.querySelector('.table-head .table-column');
        if (getHead && !firstRow){
            firstRow = getHead as HTMLElement;
            that.thead = true;

        }
        if (!firstRow) return;

        let onClick = function(){
            if (that.current && that.current !== this) {
                that.current.removeAttribute('aria-sort');
            }
            that.current = this;
            that.sortTable(this);
        };

        firstRow = Util.getElem('.table-sort', 'all', firstRow);
        firstRow.forEach(funtion(value){
            value.getAttribute('role','c')
        });
    }
}

const Util = {
    getElem(ele: HTMLElement | string, mode?: 'all' | HTMLElement | null, parent?: HTMLElement): Element | HTMLElement | HTMLElement[] | NodeListOf<Element> | null {
        if (typeof ele === 'object') {
            return ele;
        } else if (mode === undefined && parent === undefined) {
            return isNaN(Number(ele)) ? document.querySelector(ele) : document.getElementById(ele as string);
        } else if (mode === 'all' || mode === null) {
            return (parent === undefined) ? document.querySelectorAll(ele) : parent.querySelectorAll(ele);
        } else if (typeof mode === 'object' && parent === undefined) {
            return mode.querySelector(ele);
        }
        return null; // 預設返回值，如果不符合任何條件
    },

    getChildIndex(node: HTMLElement): number | false {
        // node.parentNode 可能為NULL
        if (node.parentNode&& node.parentNode !== undefined) {
            return Array.prototype.indexOf.call(node.parentNode.children, node);
        }
        return false;
    }
};
